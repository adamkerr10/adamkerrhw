fun hw1(inFile : string, outFile : string) =
	let
		val ins = TextIO.openIn inFile
		val outs = TextIO.openOut outFile
		fun helper(copt: string option) =
			case copt of
				NONE => (TextIO.closeIn ins; TextIO.closeOut outs)
				| SOME(c) => (output (stdOut, s); helper(TextIO.input1 ins))
	in
		helper(TextIO.input1 ins)
	end
val _ = hw1("C:/Users/Adam/Documents/GitHub/adamkerrhw/hw1/sample_input_1.txt", "C:/Users/Adam/Documents/GitHub/adamkerrhw/hw1/sample_output_1.txt");