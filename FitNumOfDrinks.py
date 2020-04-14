import SimPy.InOutFunctions as IO
import SimPy.Plots.Histogram as Hist
import SimPy.StatisticalClasses as Stat
import SimPy.FittingProbDist_ML as FitML

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
fit_results = FitML.fit_poisson(data=cols[0],
                                x_label='Weekly number of drinks',
                                bin_width=1)
print('Fitting a Poisson distribution:', fit_results)

# fit a gamma-Poisson distribution
fit_results = FitML.fit_gamma_poisson(data=cols[0],
                                      x_label='Weekly number of drinks',
                                      bin_width=1)
print('Fitting a gamma-Poisson distribution:', fit_results)

# fit a beta-binomial distribution
fit_results = FitML.fit_beta_binomial(data=cols[0],
                                      x_label='Weekly number of drinks',
                                      bin_width=1)
print('Fitting a beta-binomial distribution:', fit_results)
