TSP algorithms survey
=============

An animation of four algorithms trying to solve a traveling salesman problem.

### algorithms

Given a set of 200 cities four algorithms are used to find the shortest tour
of all 200 cities.  The algorithms are:

1. Random path, start a city and randomly select the next city from the remaining not visited cities until all cities are visited.
2. Greedy, start a city select as next city the unvisited city that is closest to the current city
3. 2-Opt, First create a random tour, and then optimize this with the 2-opt
   algorithm
4. Simulated Annealing. First create a random tour, and then optimize this with 2-opt in combination
   with simualted annealing.

### results

lenth | greedy | 2opt | sa | optimal | random
 --- | --- | --- | --- | --- | --- 
p15 | 284.38 | 284.38 | 284.38 | 284.38 | 818
att48 | 40526 | 35579 | 33607 | 33523 | 157530
rand200 | 36226 | 31887 | 30944 | x | 327452

time | greedy | 2opt | sa
 --- | --- | --- | --- 
p15 | 1ms | 5ms | 11.12
att48 | 6ms | .24s | 11s
rand200 | 10ms | 18s | 14.5s

### citation

If you find the code useful in your research, please consider citing:

      @article{he2017empirical,
        title={An Empirical Analysis of Approximation Algorithms for the Euclidean Traveling Salesman Problem},
        author={He, Yihui and Xiang, Ming},
        journal={arXiv preprint arXiv:1705.09058},
        year={2017}
      }

[Paper](https://github.com/yihui-he/TSP-paper) and [实验报告](https://github.com/yihui-he/TSP-report) latex code are also available.

### setups

To create the animation you will need python (Version 2) and ffmpeg.

For python you need one additional library (matplotlib) and its dependcies.
You can install it with:

    pip install matplotlib


To create the animation use:

    make .anim
    make

This should create a file called sa.mp4.  This should be playable with vlc.
