OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
creg c[5];
x q[7];
cx q[0],q[1];
cx q[2],q[6];
h q[7];
t q[1];
t q[6];
t q[7];
cx q[6],q[1];
cx q[7],q[6];
cx q[1],q[7];
tdg q[6];
cx q[1],q[6];
tdg q[1];
tdg q[6];
t q[7];
cx q[7],q[6];
cx q[1],q[7];
cx q[6],q[1];
h q[7];
cx q[1],q[6];
cx q[6],q[7];
