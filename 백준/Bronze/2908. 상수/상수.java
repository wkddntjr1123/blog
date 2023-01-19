import java.io.*;

public class Main {
    private int n;
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nums = br.readLine().split(" ");
        int a = Integer.parseInt(new StringBuilder(nums[0]).reverse().toString());
        int b = Integer.parseInt(new StringBuilder(nums[1]).reverse().toString());
        System.out.println(a < b ? b : a);
    }
    
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}