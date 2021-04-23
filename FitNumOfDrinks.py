import SimPy.InOutFunctions as IO
import SimPy.Plots.Histogram as Hist
import SimPy.Plots.ProbDist as Plot
import SimPy.RandomVariateGenerators as RVGs
import SimPy.Statistics as Stat

# read weekly number of drinks
cols = IO.read_csv_cols(file_name='dataNumOfDrinks.csv',
                        n_cols=1,
                        if_ignore_first_row=True,
                        if_convert_float=True)

# make a histogram
Hist.plot_histogram(data=cols[0],
                    title='Weekly Number of Drinks',
                    bin_width=1)

# mean and standard deviation
stat = Stat.SummaryStat(name='Weekly number of drinks',
                        data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())

# fit a Poisson distribution

# plot the fitted Poisson distribution

# fit a gamma-Poisson distribution

# plot the fitted gamma-Poisson distribution

# fit a beta-binomial distribution

# plot the fitted beta-binomial distribution
