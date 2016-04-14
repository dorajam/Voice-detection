import numpy
import theano
import theano.tensor as T

N = 60                                   # training sample size
feats = 1144                               # number of input variables

# generate a dataset: D = (input_values, target_class)
D = (numpy.random.randn(N, feats), numpy.random.randint(size=N, low=0, high=2))
training_steps = 10000

# Declare Theano symbolic variables
x = T.matrix("x")
y = T.vector("y")


class LogisticReg(object):

    def __init__(self, inp, n_in, n_out):
        self.inp = inp
        self.n_in = len(inp)
        self.n_out = 2
        
