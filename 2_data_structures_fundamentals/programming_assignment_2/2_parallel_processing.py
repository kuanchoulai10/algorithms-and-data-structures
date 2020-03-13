# Uses python3
class Worker:
    def __init__(self, nxt, idx):
        self.next = nxt  # 下個閒置時間點
        self.id = idx  # 執行緒編號


class Job:
    def __init__(self, duration):
        self.duration = duration  # 執行任務所需時間
        self.assigned_wk = None  # 哪個執行緒執行
        self.start = None  # 在哪個時間點開始執行


class JobQueue:
    def read_data(self):
        """讀取檔案，並建構執行緒物件和任務物件"""
        self.num_wks, num_jbs = map(int, input().split())
        self.wks = [Worker(0, idx) for idx in range(self.num_wks)]
        self.jbs = [Job(d) for d in list(map(int, input().split()))]
        assert num_jbs == len(self.jbs)

    def write_response(self):
        """印出結果"""
        for jb in self.jbs:
            print(jb.assigned_wk, jb.start)

    def assign_jobs(self):
        """分派任務給執行緒"""
        for jb in self.jbs:
            # 指派任務
            jb.assigned_wk = self.wks[0].id
            jb.start = self.wks[0].next
            # 更新並維持 binary min-heap 的結構
            self.wks[0].next += jb.duration
            self.sift_down(0)

    def sift_down(self, current):
        """維持 binary min-heap 的結構"""
        # `end` 負責記錄最後一個執行緒在哪，避免超出範圍
        # `target` 和 `target_wk` 負責記錄當前執行緒要與哪個子執行緒互換
        end = self.num_wks-1
        target = current
        target_wk = self.wks[target]
        # 如果左執行緒沒有超出範圍
        left = 2*current+1
        if left <= end:
            left_wk = self.wks[left]
            # 兩種情況下需要更新
            # 1. 左執行緒的下個閒置點小於目標執行緒的
            # 2. 左執行緒的下個閒置點等於目標執行緒的，且左執行緒編號小於目標執行緒的
            if (left_wk.next < target_wk.next) or (left_wk.next == target_wk.next and left_wk.id < target_wk.id):
                target = left
                target_wk = left_wk
        # 如果右執行緒沒有超出範圍
        right = 2*current+2
        if right <= end:
            # 兩種情況下需要更新
            # 1. 右執行緒的下個閒置點小於目標執行緒的
            # 2. 右執行緒的下個閒置點等於目標執行緒的，且右執行緒編號小於目標執行緒的
            right_wk = self.wks[right]
            if (right_wk.next < target_wk.next) or (right_wk.next == target_wk.next and right_wk.id < target_wk.id):
                target = right
                target_wk = right_wk
        # 如果有需要更改 binary min-heap 的結構，則進行相關操作，並進到下一層
        if current != target:
            self.wks[current], self.wks[target] = self.wks[target], self.wks[current]
            self.sift_down(target)

    def solve(self):
        """wrapper method"""
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
