**Session 2**

**Big Data:** Why Traditional Systems Fail
Big Data refers to datasets that exceed the storage, speed, and processing capabilities of traditional databases. As volume grows into terabytes and petabytes, single-machine systems face critical bottlenecks:

•	**Storage Limits:** A single server cannot scale indefinitely.

•	**Processing Latency:** Computation takes too long on non-distributed hardware.

•	**Hardware Vulnerability**: High risk of data loss upon a single point of failure.

This necessitated the move to Distributed Systems, where both data storage and computation are spread across a cluster of machines.

**Hadoop:** The Distributed Foundation
Hadoop was introduced to manage large-scale data using clusters of inexpensive commodity hardware.3 It addresses three core requirements:

**1.	Reliable Storage:** Distributing data across nodes.
**2.	Parallel Processing:** Running tasks simultaneously.
**3.	Automatic Fault Tolerance:** Managing node failures without data loss.

**HDFS (Hadoop Distributed File System)**
HDFS is the storage layer where large files are partitioned into blocks and replicated (standardly 3 times) across the cluster.

**•	NameNode**: The master node that manages metadata (file names, block locations). It does not store raw data.

**•	DataNode:** The worker nodes that store actual data blocks and perform read/write operations.

**Resource Management:** YARN
YARN (Yet Another Resource Negotiator) acts as the cluster's operating system, managing resources for various applications.

**•	Resource Manager:** The global authority that allocates resources across the cluster.

**•	Node Manager:** Monitors individual nodes and executes tasks assigned by the Resource Manager.

**MapReduce:** The Processing Paradigm

**MapReduce is a batch-processing model that works in two distinct phases:**

**•	Map Phase:** Filters and sorts data into key-value pairs.

**•	Reduce Phase:** Aggregates those pairs to produce a final result.

**•	Performance Constraint:** MapReduce is disk-based. It writes to the physical disk at every stage, leading to high I/O overhead and slow processing speeds.

**Apache Spark:** Unified In-Memory Computation
Spark was developed to solve the speed limitations of MapReduce.By processing data in RAM (In-Memory) rather than writing to disk between stages, Spark achieves significantly higher speeds, making it ideal for iterative analytics and machine learning.

**Spark Architecture**

**•	Driver Program:** The central "brain" that creates the execution plan (DAG) and coordinates tasks.

**•	Cluster Manager:** Allocates resources (e.g., YARN, Kubernetes).

**•	Executors:** Worker processes that run tasks and cache data in memory.

**Key Spark Concepts:** RDD and DAG

**•	RDD (Resilient Distributed Dataset):** Spark’s fundamental data structure.RDDs are immutable, partitioned collections that are fault-tolerant and allow for parallel in-memory processing.

**•	DAG (Directed Acyclic Graph):** A logical map of the execution steps. Spark uses the DAG to optimize the execution flow before running any actual tasks.

**Hadoop vs. Spark Comparison**

<img width="609" height="219" alt="image" src="https://github.com/user-attachments/assets/17bf726a-3b81-48ae-9b07-47db17a5a4bd" />


**Ecosystem Mapping** Conceptual components remain consistent across cloud providers:

<img width="623" height="175" alt="image" src="https://github.com/user-attachments/assets/ac4bc74b-8674-4056-a645-881c0e4815d2" />

**Data Governance and Delivery**

**•	Data Lineage:** Tracking the origin and transformation history of data.

**•	Data Cataloging:** Creating a searchable inventory of data assets (e.g, AWS Glue Catalog).

**•	Data Quality:** Implementing validation checks (null checks, schema validation) using tools like Great Expectations.

**•	Real-Time Systems:** Utilizing tools like Kafka and Spark Streaming for immediate data delivery to Dashboards (Power BI) or APIs.
