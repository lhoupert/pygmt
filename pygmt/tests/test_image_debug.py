import os
import pygmt

TEST_IMG = os.path.join(os.path.dirname(__file__), "baseline", "test_logo.png")

fig = pygmt.Figure()
fig.image(TEST_IMG, D="x0/0+w1i", F="+pthin,blue", V='d')
fig.savefig("image.png")
