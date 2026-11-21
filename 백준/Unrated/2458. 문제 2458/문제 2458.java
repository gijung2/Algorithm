

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] map = new int[N+1][N+1];

        for(int i =1; i<=M; i++){

            st= new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            map[a][b] = 1;
        }

        for(int k =1; k<=N; k++){
            for(int i=1; i<=N; i++){
                for(int j =1; j<=N; j++){

                    if(map[i][k] == 1 && map[k][j] ==1){
                        map[i][j] = 1;
                    }
                }
            }
        }
        int answer =0;
        for(int i =1; i<=N; i++){
            int cnt =0;
            for(int j =1; j<=N; j++){
                if(i == j) continue;//자기 자신임

                if(map[i][j]==1 || map[j][i]==1) cnt++;
            }

            if(cnt == N-1){
                answer++;
            }

        }
        System.out.println(answer);
    }
}
