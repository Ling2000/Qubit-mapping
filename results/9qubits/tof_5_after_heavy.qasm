OPENQASM 2.0;
include "qelib1.inc";
qreg q[9];
h q[1];
h q[6];
h q[7];
h q[12];
cx q[0],q[1];
tdg q[1];
cx q[2],q[1];
t q[1];
cx q[0],q[1];
tdg q[1];
cx q[2],q[1];
t q[1];
h q[1];
cx q[1],q[6];
tdg q[6];
cx q[5],q[6];
t q[6];
cx q[1],q[6];
tdg q[6];
cx q[5],q[6];
t q[6];
h q[6];
cx q[6],q[7];
tdg q[7];
cx q[8],q[7];
t q[7];
cx q[6],q[7];
tdg q[7];
cx q[8],q[7];
t q[7];
h q[7];
cx q[7],q[12];
tdg q[12];
cx q[13],q[12];
t q[12];
cx q[7],q[12];
tdg q[12];
cx q[13],q[12];
cx q[13],q[7];
t q[12];
tdg q[7];
h q[12];
cx q[13],q[7];
t q[13];
t q[7];
h q[7];
cx q[6],q[7];
t q[7];
cx q[8],q[7];
tdg q[7];
cx q[6],q[7];
h q[6];
t q[7];
cx q[8],q[7];
cx q[1],q[6];
t q[6];
tdg q[7];
cx q[5],q[6];
h q[7];
tdg q[6];
cx q[1],q[6];
h q[1];
t q[6];
cx q[0],q[1];
cx q[5],q[6];
t q[1];
tdg q[6];
cx q[2],q[1];
h q[6];
tdg q[1];
cx q[0],q[1];
t q[1];
cx q[2],q[1];
tdg q[1];
h q[1];
