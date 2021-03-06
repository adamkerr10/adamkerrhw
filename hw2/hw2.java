import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class hw2 {

	public static void hw2(String inFile,String outFile) throws IOException{
		FileInputStream fIn = new FileInputStream(inFile);
		FileOutputStream fOut = new FileOutputStream(outFile);
		BufferedReader bRead = new BufferedReader(new InputStreamReader(fIn));
		BufferedWriter bWrite = new BufferedWriter(new OutputStreamWriter(fOut));
		String line = null;
		int intChecker = 0;
		String numStore = "";
		String numStore1 = "";
		String numStore2 = "";
		Stack<String> stack = new Stack<String>();
		while ((line = bRead.readLine()) != null) {
			if(line.contains("push")){
				String numA = line.substring(5);
				String numB = numA.replace("\n", "");
				try{
					Integer.parseInt(numB);
					stack.push(numB);
				} catch(NumberFormatException e){
					stack.push(":error:");
				}
			}
			
			if(line.contains("pop")){
				if(stack.isEmpty()==true){
					stack.push(":error:");
				}
				else{
					stack.pop();
				}
			}
			
			if(line.contains("quit")){
				while(!stack.isEmpty()){
					bWrite.write(stack.pop());
					bWrite.newLine();
				}
				bRead.close();
				bWrite.close();
				return;
			}
			
			if(line.contains(":true:")){
				stack.push(":true:");
			}
			
			if(line.contains(":false:")){
				stack.push(":false:");
			}
			
			if(line.contains(":error:")){
				stack.push(":error:");
			}
			
			if(line.contains("add")){
				int size = stack.size();
				if(size !=0 && size != 1){
					try{
						Integer.parseInt(stack.peek());
						String num1 = stack.pop();
						intChecker = 1;
						numStore = num1;
						Integer.parseInt(stack.peek());
						intChecker = 0;
						numStore = "";
						String num2 = stack.pop();
						int int1 = Integer.parseInt(num1);
						int int2 = Integer.parseInt(num2);
						int result = int2+int1;
						String strResult = Integer.toString(result);
						stack.push(strResult);
					} catch(NumberFormatException e){
						if(intChecker == 1 && numStore != ""){
							stack.push(numStore);
						}
						stack.push(":error:");
					}
				}
				else{
					stack.push(":error:");
				}
			}
			
			if(line.contains("sub")){
				int size = stack.size();
				if(size !=0 && size != 1){
					try{
						Integer.parseInt(stack.peek());
						String num1 = stack.pop();
						intChecker = 1;
						numStore = num1;
						Integer.parseInt(stack.peek());
						intChecker = 0;
						numStore = "";
						String num2 = stack.pop();
						int int1 = Integer.parseInt(num1);
						int int2 = Integer.parseInt(num2);
						int result = int2-int1;
						String strResult = Integer.toString(result);
						stack.push(strResult);
					} catch(NumberFormatException e){
						if(intChecker == 1 && numStore != ""){
							stack.push(numStore);
						}
						stack.push(":error:");
					}
				}
				else{
					stack.push(":error:");
				}
			}
			
			if(line.contains("mul")){
				int size = stack.size();
				if(size !=0 && size != 1){
					try{
						Integer.parseInt(stack.peek());
						String num1 = stack.pop();
						intChecker = 1;
						numStore = num1;
						Integer.parseInt(stack.peek());
						intChecker = 0;
						numStore = "";
						String num2 = stack.pop();
						int int1 = Integer.parseInt(num1);
						int int2 = Integer.parseInt(num2);
						int result = int2*int1;
						String strResult = Integer.toString(result);
						stack.push(strResult);
					} catch(NumberFormatException e){
						if(intChecker == 1 && numStore != ""){
							stack.push(numStore);
						}
						stack.push(":error:");
					}
				}
				else{
					stack.push(":error:");
				}
			}
			
			if(line.contains("div")){
				int size = stack.size();
				if(size !=0 && size != 1){
					try{
						Integer.parseInt(stack.peek());
						String num1 = stack.pop();
						numStore1 = num1;
						intChecker = 1;
						numStore = num1;
						Integer.parseInt(stack.peek());
						intChecker = 0;
						numStore = "";
						String num2 = stack.pop();
						numStore2 = num2;
						int int1 = Integer.parseInt(num1);
						int int2 = Integer.parseInt(num2);
						int result = int2/int1;
						String strResult = Integer.toString(result);
						stack.push(strResult);
					} catch(NumberFormatException e){
						if(intChecker == 1 && numStore != ""){
							stack.push(numStore);
						}
						stack.push(":error:");
					} catch(ArithmeticException e){
						stack.push(numStore1);
						stack.push(numStore2);
						stack.push(":error:");
					}
				}
				else{
					stack.push(":error:");
				}
			}
			
			if(line.contains("rem")){
				int size = stack.size();
				if(size !=0 && size != 1){
					try{
						Integer.parseInt(stack.peek());
						String num1 = stack.pop();
						intChecker = 1;
						numStore = num1;
						Integer.parseInt(stack.peek());
						intChecker = 0;
						numStore = "";
						String num2 = stack.pop();
						int int1 = Integer.parseInt(num1);
						int int2 = Integer.parseInt(num2);
						int result = int2%int1;
						String strResult = Integer.toString(result);
						stack.push(strResult);
					} catch(NumberFormatException e){
						if(intChecker == 1 && numStore != ""){
							stack.push(numStore);
						}
						stack.push(":error:");
					}
				}
				else{
					stack.push(":error:");
				}
			}
			
			if(line.contains("neg")){
				int size = stack.size();
				if(size !=0){
					try{
						Integer.parseInt(stack.peek());
						String num1 = stack.pop();
						int int1 = Integer.parseInt(num1);
						int result = -int1;
						String strResult = Integer.toString(result);
						stack.push(strResult);
					} catch(NumberFormatException e){
						stack.push(":error:");
					}
				}
				else{
					stack.push(":error:");
				}
			}
			
			if(line.contains("swap")){
				int size = stack.size();
				if(size !=0 && size != 1){
						String val1 = stack.pop();
						String val2 = stack.pop();
						stack.push(val1);
						stack.push(val2);
				}
				else{
					stack.push(":error:");
				}
			}
		}
	 
	
	}
	
}
