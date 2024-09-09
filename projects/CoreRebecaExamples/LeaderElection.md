---
layout: page
title: Leader Election
permalink: /projects/CoreRebecaExamples/LeaderElection

---

#### Problem Description
A node is to be selected as a leader in a ring of n nodes. It is supposed that each node knows the nodes next to it only. The leader is selected through the messages sent among the nodes. In this ring, each node has a unique identifier. So, each node knows its own ID together with the ID’s of its neighbors. The leader is going to be the node with the least ID.
At the beginning, each node introduces itself as the leader to its neighbors. Each node compares the ID in the received message to its own leader ID, and substitutes its leader ID with the new ID received in case it is greater. If a change is made to a node’s leader ID, it will declare this change to its neighbors through messages containing the new leader ID.
The ring could be either directed or bi-directional. The node ID’s do not have to be in order; they should just be unique. Two possible algorithms for solving this problem are named LCR and HS.

#### HS Algorithm

The time order in LCR algorithm is O(n'^2^'). This time order is decreased to O(nlogn) in HS algorithm. Each node acts in a set of phases. Node i that is in phase 1, sends a message containing its ID in two directions. These messages pass through a 2'^1^' length way and then return to the sender. If both of the send messages are returned to the sender, node i will continue acting in the next phase. The sent messages might not get back to the node. When the message sent by node i moves outwards this node, every node located in its way compares its own leader ID to the ID in the message. If their own leader ID is less than the ID in the message, it will be substituted. If it is greater than it, the message will be ignored. In case they are equal, this means that the node has received its own ID, so the node selects itself as the leader.
In the returning way, nothing is done to the message and it just passes through the nodes.
The algorithm terminates when a node receives its sent messages from both sides with its own ID, and each message has passed through half of the ring.

#### LCR Algorithm
This algorithm is declared in a directed ring in which the nodes are unaware of the number of the other nodes in the ring. First, each node sends its leader ID – which is equal to its own ID at the beginning – to its right neighbor, and receives a leader ID from its left neighbor. If the received lead ID is greater than its own leader ID, it will substitute its leader ID with the new ID and declares this change to its right neighbor. If the received leader ID is less than a node’s leader ID, it will be ignored. In case the received leader ID is equal to the node’s leader ID, the node will be considered as the real leader, and the algorithm terminates.

#### Related Files
* Rebeca Model for HS Algorithm [ [zip] ](/assets/projects/Sysfier/case-studies/Leader-Election-HS.zip)
* Rebeca Model for LCR Algorithm [ [zip] ](/assets/projects/Sysfier/case-studies/Leader-Election-LCR.zip)
