# Import
from library import *
import matplotlib.pyplot as plt

"""
    Run Ant Colony Optimization (ACO) algorithm for a given Symmetric traveling salesman problem (TSP)
    @arg
        {string} tsp    -- The TSP file src name (located in /data folder)

    @export
        {results}       -- Generated files for results
        {plots}         -- Generated files for plots
"""
def test(tsp):
    # Default arguments
    '''
        iterations {80}     -- Number of iterations (Ending condition)
        colony {50}         -- Number of ants in the colony
        alpha {1.0}         -- Alpha algorithm parameter, more or less weight to a selected distance
        beta {1.0}          -- Beta algorithm parameter, more or less weight to a selected distance
        del_tau {1.0}       -- Delta Tau algorithm parameter, pheromones releasing rate
        rho {0.5}           -- Rho algorithm parameter, pheromones evaporation rate
    '''

    # Configuration vars
    n = 3                   # Repetitions

    # Algorithm Parameters
    iterations = 80
    colony = 50
    alpha = 1
    beta = 1
    del_tau = 1.0
    rho = 0.5

    results = np.zeros(n)   # Store

    # Get TSP data
    src = getTspData('data/{}.tsp'.format(tsp))
    space = None
    space = np.array(src['node_coord_section'])

    # Inform
    msg('Computing {} times for {}'.format(n, tsp))

    # Save space plot
    saveSpacePlot(tsp, space)

    # Repeat and save path plot for each result
    for i in range(n):
        # Run
        min_path, min_distance = runAcoTsp(space, iterations, colony, alpha, beta, del_tau, rho)

        # Store result
        results[i] = min_distance

        # Save path plot
        savePathPlot(i, n, tsp, space, min_path, min_distance)

    # Save results txt
    saveResultsTxt(src, results, iterations, colony, alpha, beta, del_tau, rho)

"""
    Save Space plot
    @arg
        {string} tsp            -- The TSP file src name
        {numpy.ndarray} space   -- The space

    @export
        {png}                   -- Generated .png for TSP space plot
"""
def saveSpacePlot(tsp, space):
    # Plot nodes
    plt.scatter(space[:, 0], space[:, 1], s = 15)

    # Plot properties
    plt.title('Space for {}'.format(tsp))
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')

    # Save plot
    file = 'results/{}-space.png'.format(tsp)
    plt.savefig(file)

    # Close plot
    plt.close()

    # Inform
    msg('{} generated'.format(file))

"""
    Save Path plot for a given result
    @arg
        {int} i                 -- The result
        {int} n                 -- The total results
        {numpy.ndarray}         -- Indexes of the minimun distance path for the result
        {float}                 -- the minimun distance for the result
        {string} tsp            -- The TSP file src name
        {numpy.ndarray} space   -- The space

    @export
        {png}                   -- Generated .png for ACO-TSP path result plot
"""
def savePathPlot(i, n, tsp, space, min_path, min_distance):
    # Plot nodes
    plt.scatter(space[:, 0], space[:, 1], marker='o', s = 15)
    plt.plot(space[min_path, 0], space[min_path, 1], c='g', linewidth=0.8, linestyle="--")

    # Plot properties
    plt.suptitle('Mininum Path for {}'.format(tsp))
    plt.title('Result #{} of {} for a minimum distance of {}'.format(i + 1, n, min_distance), fontsize = 10)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')

    # Save plot
    file = 'results/{}-path-{}.png'.format(tsp, i + 1)
    plt.savefig(file)

    # Close plot
    plt.close()

    # Inform
    msg('{} generated'.format(file))

"""
    Save results for a given TSP
    @arg
        {dict} src                  -- The TSP file src
        {numpy.ndarray} results     -- The TSP file as dictionary
        {int} iterations {80}       -- Number of iterations (Ending condition)
        {int} colony {50}           -- Number of ants in the colony
        {float} alpha {1.0}         -- Alpha algorithm parameter, more or less weight to a selected distance
        {float} beta {1.0}          -- Beta algorithm parameter, more or less weight to a selected distance
        {float} del_tau {1.0}       -- Delta Tau algorithm parameter, pheromones releasing rate
        {float} rho {0.5}           -- Rho algorithm parameter, pheromones evaporation rate

    @export
        {txt}                       -- Generated .txt for ACO-TSP results
"""
def saveResultsTxt(src, results, iterations, colony, alpha, beta, del_tau, rho):
    # Open or create
    file = 'results/{}-results.txt'.format(src['name'])
    txt = open(file, 'w+')

    # Write file
    txt.write('\n--------------------------')
    txt.write('\n 1- TSP INFO')
    txt.write('\n--------------------------')
    txt.write('\nNAME           : {}.tsp (stored in /data)'.format(src['name']))
    txt.write('\n# OF NODES     : {}\n'.format(src['dimension']))

    txt.write('\n--------------------------')
    txt.write('\n 2- ALGORITHM PARAMETERS')
    txt.write('\n--------------------------')
    txt.write('\nITERATIONS     : {}'.format(iterations))
    txt.write('\nCOLONY         : {}'.format(colony))
    txt.write('\nALPHA          : {}'.format(alpha))
    txt.write('\nBETA           : {}'.format(beta))
    txt.write('\nDEL_TAU        : {}'.format(del_tau))
    txt.write('\nRHO            : {}\n'.format(rho))

    txt.write('\n--------------------------')
    txt.write('\n 3- RESULTS ')
    txt.write('\n--------------------------')
    txt.write('\nMIN_DISTANCES      : {}'.format(results))
    txt.write('\n# OF RESULTS       : {}'.format(results.size))
    txt.write('\nAVG_MIN_DISTANCE   : {}'.format(np.average(results)))
    txt.write('\n--------------------------')

    # Close file
    txt.close()

    # Inform
    msg('{} generated'.format(file))

"""
    Show a console message
    @arg
        {string} str
"""
def msg(str):
    print('[Testing ACO_TSP] {}'.format(str))

"""
    Show a console message
    @arg
        {string} str
"""
def main():
    # Test for each stored TSP data
    test('kroA100')
    test('berlin52')

    # Inform
    msg('All files generated, see /results for details')

if __name__ == '__main__':
    main()
