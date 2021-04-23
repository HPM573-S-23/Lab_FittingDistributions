import SimPy.InOutFunctions as IO
import SimPy.Plots.Histogram as Hist
import SimPy.Plots.ProbDist as Plot
import SimPy.RandomVariateGenerators as RVGs
import SimPy.Statistics as Stat

# read interarrival times
cols = IO.read_csv_cols(file_name='dataInterarrivalTimes.csv',
                        n_cols=1,
                        if_ignore_first_row=True,
                        if_convert_float=True)

# make a histogram
Hist.plot_histogram(data=cols[0],
                    title='Interarrival Times (Minutes)',
                    bin_width=0.5)

# mean and standard deviation
stat = Stat.SummaryStat(name='Interarrival times',
                        data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())

# fit an exponential distribution

# plot the fitted exponential distribution


# fit a gamma distribution

# plot the fitted gamma distribution

# fit a log-normal distribution

# plot the fitted log-normal distribution