import java.io.*;
import java.util.Arrays;

public class Main {
    private int n;
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nums = br.readLine().split(" ");
        if(Integer.parseInt(nums[0])!=1 && Integer.parseInt(nums[0])!=8){
            System.out.println("mixed");
            return;
        }
        int startNum = Integer.parseInt(nums[0]) - Integer.parseInt(nums[1]) > 0 ? 8 : 1;
        int res = 0;
        for(int i=startNum; i<8; i++){
            res += Integer.parseInt(nums[i-1])  == i ? 1 : 0;
        }
        for (int i=startNum; i>1; i--){
            res += Integer.parseInt(nums[8-i])  == i ? 1 : 0;
        }
        if(res!=7){
            System.out.println("mixed");
            return;
        }
        System.out.println(startNum==1 ? "ascending" : "descending");

    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}