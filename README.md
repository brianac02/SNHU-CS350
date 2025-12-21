# SNHU-CS350

Briefly explain the work that you did on this project: What code were you given? What code did you create yourself?

    All of the helper functions, variables, and supplementary classes for this project were provided. The code that was 
    ultimately up to me to create was the actual deep Q-learning algorithm for the neural network. Doing so entailed 
    implementing a training loop which learned to navigate a maze through interaction with the environment. In each 
    epoch, the agent begins by selecting a random, valid position and selects an action utilizing an epsilson-greedy
    approach which balances exploration and exploitation. Experiences from each step are then stored in a replay buffer
    and sampled to train the network used to approximate the Q-function. A target network is used to stabilize the
    training, and metrics are gathered to evaluate the overall performance of the algorithm.

Connect your learning from throughout this course to the larger field of computer science:
  What do computer scientists do and why does it matter?

    Computer science in itself is a very broad subject, and as such, it's hard to put a perfectly-fit lid on what exactly
    it is that they do. Generally speaking, though, computer scientists are innovators and problem solvers that strive to
    solve the issues and meet the needs of the public through technology. They invent and write programs that are
    (generally) meant to improve the lives of others by making a process easier, providing entertainment, so on and so
    forth. Not every program or script or piece of technology necessarily does that, but that's the general goal. 
    
  How do I approach a problem as a computer scientist?

    I approach each problem as a computer scientist with curiosity and open-mindedness. I try to work through something
    mentally before I write any code, to think about how to get from a to b, and there's never a point when I'm writing
    code where I'm not trying to think of a better, new, more optimal and creative way of writing my code. I try to 
    pick up and learn a lot from other peope's code that I read, as well. One thing I tend to struggle with is that I 
    need to finish one thing before I move on to the next, so when I get stuck somewhere, it's near impossible for me to
    avoid for the moment and come back to. 
    
  What are my ethical responsibilities to the end user and the organization?

    There are many ethical responsibilities that I have to the end user and the organization. Maintaining both the image
    and the reputation of the organization are important, as much as the user's privacy and personal rights. I am 
    responsible for being honest and forthcoming to the company - writing legitimate and non-harmful code. Similarly, I 
    am responsible for protecting confidential data of users and not using any of it in ways unspecified or for some 
    sort of personal gain. 
