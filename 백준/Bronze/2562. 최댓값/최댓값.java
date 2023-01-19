import java.io.*;

public class Main {
    private int n;
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int maxNum=0, maxIdx=0;
        for(int i=0; i<9; i++){
            int num = Integer.parseInt(br.readLine());
            if(num > maxNum){
                maxNum = num;
                maxIdx = i+1;
            }
        }
        System.out.print(maxNum + "\n" + maxIdx);
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}