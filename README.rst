=============
bootstrapping
=============


.. image:: https://img.shields.io/pypi/v/bootstrapping.svg
        :target: https://pypi.python.org/pypi/bootstrapping

.. image:: https://img.shields.io/travis/knathanieltucker/bootstrapping.svg
        :target: https://travis-ci.org/knathanieltucker/bootstrapping

.. image:: https://readthedocs.org/projects/bootstrapping/badge/?version=latest
        :target: https://bootstrapping.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/knathanieltucker/bootstrapping/shield.svg
     :target: https://pyup.io/repos/github/knathanieltucker/bootstrapping/
     :alt: Updates


Statistical Library for Bootstrapping


* Free software: MIT license
* Documentation: https://bootstrapping.readthedocs.io.


Resources
--------

General Resources:

1. `What Teachers Should Know About the Bootstrap <http://amstat.tandfonline.com/doi/full/10.1080/00031305.2015.1089789#.Wj7iayOZPXE>`
2. `Introduction to the Bootstrap <https://www.amazon.com/Introduction-Bootstrap-Monographs-Statistics-Probability/dp/0412042312>`
2. `When the bootstrap doesn’t work <http://notstatschat.tumblr.com/post/156650638586/when-the-bootstrap-doesnt-work>`
3. `Second Thoughts on the Bootstrap <http://finmath.stanford.edu/~ckirby/brad/papers/2003SecondThoughts.pdf>`
3. `Bootstrap Confidence Intervals <https://projecteuclid.org/download/pdf_1/euclid.ss/1032280214>`
3. TODO: `Statistics: Unlocking the Power of Data <https://www.wiley.com/en-us/Statistics%3A+Unlocking+the+Power+of+Data-p-9780470601877>`
4. TODO: `Bootstrap Methods and their Application <http://www.cambridge.org/asia/catalogue/catalogue.asp?isbn=9780521574716>`
5. TODO (A lot of goodies in here, probably to be checked out once the basics are done) `Bootstrap Methods with Applications to R <http://www.ievbras.ru/ecostat/Kiril/R/Biblio/R_eng/Chernick2011.pdf>`

Code Resources
`Python <https://github.com/facebookincubator/bootstrapped/tree/master/bootstrapped>`
`Julia <https://github.com/juliangehring/Bootstrap.jl>`
`Simple Python <https://github.com/christopherjenness/bootstrap/tree/master/bootstrap>`
This one is pretty deep, will be good to go through once other features have been implemented `R <https://github.com/christopherjenness/bootstrap/tree/master/bootstrap>`


Features
--------

Sampling procedures
******

Make parallel. Make sparse??

Good stuff `here <https://github.com/facebookincubator/bootstrapped/tree/master/bootstrapped>`
for checking out thread safe plus sparse arrays.

Though the initial implementation should be thread safe iterators that can be materialized into sparse representations of the original data.
You should be able to yield batches as well.

To do the more complicated sampling methods we can see `Julia <https://github.com/juliangehring/Bootstrap.jl>`

1. With/without replacement
2. Antithetic resampling
2. Balanced random resampling
2. Exact resampling, iterating through all unique resamples
2. Resampling of residuals in generalized linear models (question on whether to do this here or with the regressions below)

2. Jackknife... Maybe this should just be joined with the more complex methods
3. Parametric sampling

Sampling Statistics
******

1. Standard Error
2. Bias estimates

Confidence Intervals
******

For these we can see `Julia <https://github.com/juliangehring/Bootstrap.jl>`

1. Student t intervals
2. Normal intervals
3. Percentile Intervals
4. BCA
5. ABC

Regression
******

Tests
******
Permutation Tests
Bootstrap Hypothesis Testing
Power calculations Good stuff `here <https://github.com/facebookincubator/bootstrapped/tree/master/bootstrapped>` This will be useful for checking out the visualizations they include with the power calc

Calibration
******

General Features
******

* Optimize number of bootstrap replications with coef of var and time
* Time estimates of replications (on multiple cores)
* Estimates of error in bootstrap estimates (Intro to the Boot, 19)
* Efficiency: (Intro to the Boot, 23)

Meta Features
******

Perhaps have a general multisample tool, though looks like we might just be able to build it into specific areas above.
