def numpydata_from_csv(csv_file):
    tmp_data = pandas.read_csv(csv_file, header =None) 
    data = tmp_data.to_numpy()
    return data

def plot_year_vs_total_CO2_emissions(name, CO2_Emissions):
    plt.plot([0.5, 1, 10],[CO2_Emissions])
    plt.axis([0, 12, 0, 100])
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions')
    plt.title('CO2 Emissions By Year' % name)
    plt.show()
    return


def dynamic_plot():
    xx= input ("Which column do you want to plot: ")
    x = data[0,int(xx)]
    yy= input ("What's the x axis label: ")
    plt.xlabel(str(yy))
    zz= input ("What's the y axis label: ")
    plt.ylabel(str(zz))
    aa= input ("What's the graph title: ")
    plt.title (str(aa))
    plt.show()
