import numpy as np

class GameExperience(object):

    def __init__(self, model, target_model, max_memory=100, discount=0.95):
        self.model = model
        self.target_model = target_model
        self.max_memory = max_memory
        self.discount = discount
        self.memory = list()
        self.num_actions = model.output_shape[-1]

    def remember(self, episode):
        self.memory.append(episode)
        if len(self.memory) > self.max_memory:
            del self.memory[0]

    def predict(self, envstate):
        return self.model.predict(envstate, verbose=0)[0]

    def get_data(self, data_size=10):
        mem_size = len(self.memory)
        if mem_size == 0:
            return None, None

        data_size = min(mem_size, data_size)
        batch_indices = np.random.choice(mem_size, data_size, replace=False)

        env_size = self.memory[0][0].shape[1]

        inputs = np.zeros((data_size, env_size), dtype=np.float32)
        next_inputs = np.zeros((data_size, env_size), dtype=np.float32)
        actions = np.zeros(data_size, dtype=np.int32)
        rewards = np.zeros(data_size, dtype=np.float32)
        game_overs = np.zeros(data_size, dtype=bool)

        for i, j in enumerate(batch_indices):
            envstate, action, reward, envstate_next, game_over = self.memory[j]
            inputs[i] = envstate[0]
            next_inputs[i] = envstate_next[0]
            actions[i] = action
            rewards[i] = reward
            game_overs[i] = game_over

        current_q = self.model.predict(inputs, verbose=0)
        next_q = self.target_model.predict(next_inputs, verbose=0)

        targets = current_q.copy()

        for i in range(data_size):
            if game_overs[i]:
                targets[i, actions[i]] = rewards[i]
            else:
                targets[i, actions[i]] = rewards[i] + self.discount * np.max(next_q[i])

        return inputs, targets