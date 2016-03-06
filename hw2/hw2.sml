fun checkLetter(l, []) = false
  | checkLetter(l, x::xs) =
      if x = l
      then true
      else checkLetter(l, xs)	  

fun checkAlpha([], input) = true
  | checkAlpha(x::xs, input) =
      if checkLetter(x, input)
      then checkAlpha(xs, input)
      else false;
	  
fun hw2(inFile : string, outFile : string) =
	let
		val fileInp = TextIO.openIn inFile
		val fileOut = TextIO.openOut outFile
		val testo = TextIO.inputLine fileInp
		fun check_pangram(testo : string option) =
				let
						val test = getOpt(testo," ")
						val _ = print(test)
						val str = "abcdefghijklmnopqrstuvwxyz"
						val strList = String.explode(str)
						val testList = String.explode(test)	
						val res = Bool.toString(checkAlpha(strList, testList))
						val _ = print(res)
						val res = res ^ "\n"
						val _ = TextIO.output (fileOut, res)
						val _ = TextIO.flushOut(fileOut)
				in 
					true
				end
		fun helper(testo : string option) = 
			case testo of
				NONE => ( TextIO.closeIn fileInp; TextIO.closeOut fileOut)
			| SOME(c) => ( check_pangram( testo );
			helper(TextIO.inputLine fileInp))
	
	in 
		helper(testo)
	end

val _ = hw2("sample_input_1.txt","sample_output_1.txt")
val _ = hw2("sample_input_2.txt","sample_output_2.txt")
val _ = hw2("sample_input_3.txt","sample_output_3.txt")