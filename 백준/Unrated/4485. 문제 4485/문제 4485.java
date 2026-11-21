
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = 1;

        while (true) {
            int N = Integer.parseInt(br.readLine());

            if (N == 0) break;

            int[][] map = new int[N][N];
            int[][] dist = new int[N][N];

            for (int i = 0; i < N; i++) {
                Arrays.fill(dist[i], 100_000_000);
            }

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
                return Integer.compare(a[2], b[2]);
            });

            dist[0][0] = map[0][0];
            pq.add(new int[]{0, 0, dist[0][0]});

            while (!pq.isEmpty()) {
                int[] c = pq.poll();
                int curx = c[0];
                int cury = c[1];
                int curweight = c[2];

                if (curweight > dist[curx][cury]) continue;

                for (int d = 0; d < 4; d++) {
                    int nr = curx + dr[d];
                    int nc = cury + dc[d];

                    if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

                    int nextweight = curweight + map[nr][nc];

                    if (nextweight < dist[nr][nc]) {
                        dist[nr][nc] = nextweight;
                        pq.add(new int[]{nr, nc, nextweight});
                    }
                }
            }

            System.out.println("Problem " + tc + ": " + dist[N - 1][N - 1]);
            tc++;
        }
    }
}
