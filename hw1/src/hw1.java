import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class hw1 {
	public static void hw1(String inFile,String outFile) throws IOException{
		FileInputStream fIn = new FileInputStream(inFile);
		FileOutputStream fOut = new FileOutputStream(outFile);
		BufferedReader bRead = new BufferedReader(new InputStreamReader(fIn));
		BufferedWriter bWrite = new BufferedWriter(new OutputStreamWriter(fOut));
		String line = null;
		while ((line = bRead.readLine()) != null) {
			int i = 0;
			for(char c : line.toCharArray()) {
		        int x = Character.toLowerCase(c);
		        if (x >= 'a' && x <= 'z') {
		            i |= 1 << (x - 'a');
		        }
		    }
		    if (i == (i | ((1 << (1 + 'z' - 'a')) - 1))) {
		    	bWrite.write("true");
				bWrite.newLine();
		    }
		    else{
		    	bWrite.write("false");
		    	bWrite.newLine();
		    }
		}
	 
		bRead.close();
		bWrite.close();
	}
	}

