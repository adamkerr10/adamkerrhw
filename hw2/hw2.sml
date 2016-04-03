fun hw1(inFile : string, outFile : string) =
	let
		val ins = TextIO.openIn inFile
		val outs = TextIO.openOut outFile
		val lines = TextIO.inputLine fileInp
		fun helper(copt: string option) =
			case lines of
				NONE => (TextIO.closeIn ins; TextIO.closeOut outs)
				| SOME(c) => (output (stdOut, s); helper(TextIO.inputLine fileInp))
	in
		helper(lines)
	end
