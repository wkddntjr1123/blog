import java.io.*;

public class Main {
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            int seqCount = 0;
            int result = 0;
            for(char c: br.readLine().toCharArray()){
                if(c=='X'){
                    seqCount = 0;
                    continue;
                }
                result += ++seqCount;
            }
            System.out.println(result);    
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}