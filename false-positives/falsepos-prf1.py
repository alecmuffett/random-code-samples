#!/usr/bin/env python
import random

class Ansi:
    END     =  '\033[0m'
    BOLD    =  '\033[1m'
    UL      =  '\033[4m'
    BLACK   =  '\033[90m'
    RED     =  '\033[91m'
    GREEN   =  '\033[92m'
    YELLOW  =  '\033[93m'
    BLUE    =  '\033[94m'
    MAGENTA  = '\033[95m'
    CYAN  = '\033[96m'
    WHITE  = '\033[97m'

items = 10000000 # ie: 10 million items
badness_rate = 10000 # ie: 1 in 10,000 items are bad
test_accuracy_pct = 99.5 # ie: 99.5% accurate test

results = dict()
results['accurate:good'] = 0
results['accurate:bad'] = 0
results['inaccurate:good'] = 0
results['inaccurate:bad'] = 0

test_accuracy = test_accuracy_pct / 100 # normalise: 99% -> 0.99

def test(x):
    r = random.random()
    if r <= test_accuracy: # the test is accurate
        results['accurate:'+x] += 1
    else:
        results['inaccurate:'+x] += 1

for i in range(0, items):
    test('bad' if ((i % badness_rate) == 0) else 'good')

print 'tested %s%d items%s where %s1 in %d are bad%s, with %s%.5f%% test accuracy%s' % (
    Ansi.MAGENTA, items, Ansi.END,
    Ansi.YELLOW, badness_rate, Ansi.END,
    Ansi.CYAN, test_accuracy_pct, Ansi.END,
)

tn = results['accurate:good']
tp = results['accurate:bad']
fp = results['inaccurate:good']
fn = results['inaccurate:bad']
p = float(tp)/(tp+fp)
r = float(tp)/(tp+fn)
f1 = 2 * ((p*r)/(p+r))
print '%s: %s%d%s' % ('good items, correctly identified', Ansi.GREEN, tn, Ansi.END)
print '%s: %s%d%s' % ('bad items, correctly identified', Ansi.GREEN, tp, Ansi.END)
print '%s: %s%d%s' % ('good items, false positive as bad', Ansi.RED, fp, Ansi.END)
print '%s: %s%d%s' % ('bad items, false negative as good', Ansi.RED, fn, Ansi.END)
print 'p={0} r={1} f1={2}'.format(p, r, f1)
