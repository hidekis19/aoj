
def main(N, M, C, X):
    dp = [[INF] * 256 for _ in range(N+1)]
    dp[0][128] = 0

    for i in range(1, N+1):
        for j in range(256):

            for k in range(M):
                next_j = j + C[k]
                next_j = max(0, min(255, next_j))

                dp[i][next_j] = min(dp[i][next_j],
                                    dp[i-1][j] + pow(next_j - X[i-1], 2))

    answer = min(dp[N][:])

    return answer


if __name__ == "__main__":
    INF = float('inf')
    answer_list = []
    while True:

        N, M = map(int, input().split()) # Nが入力の数、Mがコードブックの数字の数
        if N == M == 0:
            break

        C = [int(input()) for _ in range(M)] # コードブック
        X = [int(input()) for _ in range(N)] # 入力値

        answer_list.append(main(N, M, C, X))

    for answer in answer_list:
        print(answer)

