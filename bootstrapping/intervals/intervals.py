"""

Called intervals because we might put belief intervals as well as CIs in here.

This should be able to work on either generators/iters (thread and not threadsafe) as well as arrays

Should be parallel when we want it to be. And we should keep the avail to operate on batches

"""
from sampling.sampling import basic_sampling

# certainly a smarter way to do this
SAMPLING_METHODS = {
    'basic_sampling': basic_sampling
}


def percentile_confidence_interval(x,
                                   alpha=.05,
                                   sampling_method='basic_sampling',
                                   batch_size=1,
                                   num_workers=1) # not sure if num_workers is the appropriate var that we will need
    pass
