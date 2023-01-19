import java.io.*;

public class Main {
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long mul = 1;
        for(int i=0; i<3; i++){
            mul *= Long.parseLong(br.readLine());
        }
        String str = Long.toString(mul);
        int[] idxArr = new int[10];
        for(int i = 0; i<str.length(); i++){
            idxArr[Integer.parseInt(""+str.charAt(i))]++;
        }
        for(int count:idxArr){
            System.out.println(count);
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}