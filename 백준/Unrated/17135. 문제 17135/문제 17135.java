import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    //캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임임.
    //게임이 진행되는 곳은 크기가 N*M인 격자판으로 나타냄.
    //각칸에 포함된 적의수는 최대하나, 격자판의 N번행의 바로아래 모든 칸에는 성이 있음.
    //성을 적에게서 지키기 위해 궁수 3명을 배치하고자 함. 궁수는 성에 배치함.
    //각각의 턴마다 궁수는 적하나를 공격가능, 모든 궁수는 동시에 공격함.
    //궁수가 공격하는 적은 거리가 D이하인 적중에서도 가장 가까운적임.
    // 그러한 적이 여럿일 경우 가장 왼쪽에 있는 적을 공격(열에 수가 작은)
    //궁수의 공격이 끝나면 적은 이동, 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외,
    //모든 적이 격자판에서 제외 되면 게임 이끝남.
    //궁수의 공격으로 제거할수 있는 적의 최대 수를 계산

    static int N, M, K;
    static int[][]map;
    static int archer[];
    static int answer;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        answer = 0;
        archer = new int[3];
        map = new int[N][M];
        int enemeycnt = 0;
        for(int i =0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<M; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] ==1){
                    enemeycnt++; //적의 수 채킹
                }
            }
        }

        //dfs(시뮬)
        dfs(0, 0);
        //출력
        System.out.println(answer);
    }

    public static void dfs(int start, int cnt){

        //조합에서 뽑은개수가 3이되면
        if(cnt == 3){
            simulate();
            //시뮬돌려서 최대값 갱신
            return;
        }

        for(int i= start; i<M; i++){

            archer[cnt] = i;
            dfs(i+1, cnt+1);

        }

    }

    public static void simulate(){
        //복사한 배열에서하기
        int[][]copy = new int[N][M];

        for(int i = 0; i<N; i++){
            copy[i] = map[i].clone();
        }

        int kill = 0;

        for(int turn = 0; turn <N; turn++){
            int[][] target = new int[3][2];
            //궁수 3명이 공격할 좌표를 선택
            for(int a= 0; a<3; a++){
                int mindist = Integer.MAX_VALUE;
                int mincol = Integer.MAX_VALUE;

                target[a][0] = -1;
                target[a][1] = -1;

                for(int r=0; r<N; r++){
                    for(int c = 0; c<M; c++){
                        if(copy[r][c] == 0) continue;

                        int dist = Math.abs(N-r)+ Math.abs(archer[a] - c);

                        if(dist>K) continue;

                        //거리가 더짧거나
                        //거리가 같으면서 더 왼쪽인 적 선택
                        if(dist<mindist || (dist == mindist && c<mincol)) {
                            mindist = dist;
                            mincol = c;

                            target[a][0] = r;
                            target[a][1] = c;

                        }

                    }
                }
            }
            //선택된 좌표들을 한 번에 제거, 이미 제거된 적은 중복 카운트 x
            //살아 있는 적은 한 칸 아래로 이동

            for(int a= 0; a<3; a++){
                int r= target[a][0];
                int c= target[a][1];

                if(r ==-1) continue;

                if(copy[r][c] ==1){
                    copy[r][c] = 0;
                    kill++;
                }
            }

            for(int r= N-1; r>=1; r--){
                copy[r] = copy[r -1].clone();
            }

            for(int c= 0; c<M; c++){
                copy[0][c] = 0;
            }
        }
        answer = Math.max(answer, kill);

    }
}