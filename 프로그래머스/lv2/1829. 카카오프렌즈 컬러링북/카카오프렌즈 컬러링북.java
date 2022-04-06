class Solution {
    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};
    static int cnt = 0;
    void dfs(int[][] picture ,int x, int y, boolean[][] visited){
        visited[x][y]= true;
        cnt += 1;
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0<=nx && nx<visited.length && 0<=ny && ny<visited[0].length && picture[nx][ny]==picture[x][y] && !visited[nx][ny]){
                    dfs(picture,nx,ny,visited);
            }
        }
    }
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        boolean[][] visited = new boolean[m][n];
        for(int i=0; i< m; i++){
            for(int j=0; j<n; j++){
                if(picture[i][j]!=0 && !visited[i][j]){
                    numberOfArea += 1;
                    cnt = 0;
                    dfs(picture, i,j,visited);
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, cnt);
                }
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    public static void main(String [] args){
        Solution s = new Solution();
        int[][] test = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
        s.solution(6,4,test);
    }
}