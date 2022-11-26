# ScalableCapital Utils

This repository contains a Python package that's intended to fix the lack of an export functionality for transactions on the [ScalableCapital](https://scalable.capital) broker.
It works by parsing the HTML page of the transaction history and transforming into a Python data structure.

A few warnings should be issued at this point:

* This is a minimal effort solution, so it's far from giving you elaborate evaluation tools.
* ScalableCapital might change their HTML structure at any time, so this package might break at any time.
* The package is not unit tested, so it might contain bugs.
* The package is currently biased for the german version of the website, so it might not work well for other languages.

## How to use

Log in on the ScalableCapital website and navigate to the [transaction history page](https://scalable.capital/transactions).
Scroll down to the bottom of the page to load all transactions.
Then save the page as HTML file.
Finally, plug in the path to that HTML fail into `main.py`.
Before running the script, make sure to install the dependencies with `pip install -r requirements.txt`.

## Scope, Support, Stability & Contributing

I consider this mostly a private project for my personal usage (and education).
As such, I won't put particular effort in maintaining a stability policy.
I will also most likely not accept feature requests (until I like them myself) or offer support.
If you coded some extension (e.g. language support) of or fix for this project you're however very welcome to send a pull request.