"""
COMS W4701 Artificial Intelligence - Programming Homework 4

A Q-learning agent for a stochastic task environment

@author: YOUR NAME AND UNI
"""

import random
import math
import sys


class Qlearner(object):

    def __init__(self, states, valid_actions, parameters):
        self.alpha = parameters["alpha"]
        self.epsilon = parameters["epsilon"]
        self.gamma = parameters["gamma"]
        self.Q0 = parameters["Q0"]

        self.states = states
        self.Qvalues = {}
        for state in states:
            for action in valid_actions(state):
                self.Qvalues[(state, action)] = parameters["Q0"]

    def setEpsilon(self, epsilon):
        self.epsilon = epsilon

    def setDiscount(self, gamma):
        self.gamma = gamma

    def setLearningRate(self, alpha):
        self.alpha = alpha


    def update(self, state, valid_actions, transition):
        """
        Perform one transition from state and update the corresponding Q-value.
        Choose an action using epsilon-greedy and valid_actions(state).
        transition(state, action) returns a (successor, reward) pairing.
        self.Qvalues is updated in place and the successor state is returned.
        """
        #### REPLACE THE FOLLOWING WITH YOUR CODE ###
        new_state, reward = transition(state, random.choice(valid_actions(state)))
        return new_state


    def run_Qlearning(self, valid_actions, transition, num_episodes):
        """
        Run Q-learning for num_episodes and then returns the set of all Qvalues.
        valid_actions(state) and transition(state, action) are functions passed into update().
        """
        for i in range(num_episodes):
            state = random.choice(tuple(self.states))
            while state is not None:
                state = self.update(state, valid_actions, transition)
        return self.Qvalues
