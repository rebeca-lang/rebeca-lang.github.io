---
layout: page
title: Commit Problem
permalink: /allprojects/CoreRebecaExamples/CommitProblem

---

#### Problem Description
There are n entities that are supposed to commit on performing an action. In case any of them disagrees, the action will be aborted. In other words:
 Commit = entity1.commit AND entity2.commit AND ...

#### Algorithm
A possible algorithm for solving this problem is to suppose one of the entities is the listener and the others are senders. The listener collects the other entities commit/abort messages (and also it’s own message). If no abort messages are received, the final commit message will be sent to all entities. If there is an abort message, the final message sent to everyone would be an abort message.

#### Related Files
* The specification of the model [ [zip] ](/assets/projects/CoreRebeca/case-studies/Commit-Problem.zip)
