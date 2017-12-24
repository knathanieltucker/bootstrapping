"""
There may need to be a time when this file will need to get factored out into its parts.

These functions should be thread safe iterators (or generators -- whichever is faster), which yeild batches of their results.

There should be functionality to materialize them into sparse thingys or something with good perf

"""

def basic_sampling(x, batch_size=1, replacement=True):
    pass
