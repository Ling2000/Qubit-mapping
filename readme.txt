Python version:3.7 
Please make sure you Python can compile it normally

It assumes that all circuits and couplings are valid. Thus, it will not check whether this circuit or coupling is valid.

It assumes that the number of qubit or register begins from 0.

Please put the circuit testcases in a folder under the circuits folder. For example, if you want to test the 3qubits/3_17_13.qasm,you should put 3qubits into the circuits at first and then put the 3_17_13.qasm into folder circuits/3qubits.

You should select mode at first. You will see "Please choose mode: folder or file(If you want to test folder, please input fo. If you want to test file, please input fi):" print at secreen firstly. If you want to test the all the circuits in a folder under the folder circuits, you need to input fo.

Input example: small/3_17_13.qasm qx2.txt
	       Then it will print the initial map or "no" in the screen and output the new qasm into results/small 

Input example2: small qx2.txt

Then it will print the initial map for all circuits in the folder small in the screen and output the new qasm into results/small 