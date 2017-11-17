Requirements:
- g++ (or any other C++ compiler)
- Operating System: Windows or Unix - tested under Mac, Windows, Fedora and Debain GNU/Linux.
    (Some Unix shell scripts are already provided.)

Execution:
To execute each sample, you should compile both model checking server and the sample source codes. You can find the server codes in "Server" folder. After compilation of server folder content, you can start server by running the executable file. Executable file reads configuration parameters from "serverproperties.txt". This file contains listening port number and number of connecting clients.
The samples source codes are in the "train", "resource" and "phils" folders. You can compile source codes of one of them and execute the result file. The result file should be executed using "-bfs" parameter. The connecting server configuration are set using the property file of "serverproperties.txt". To disable a distributed technique, one needs to comment out the line defining DISTRIBUTED_BFS and MESSAGE_PATH_BASED_DISTRIBUTION in "Types.h" and recompile the C++ files again. In case of random model checking, random distribution and CDG based distributions are enabled by defining the above words respectively.

Note that using compile-time conditions avoids unnecessary checks during run-time!