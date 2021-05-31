"""
Schedule DB SchedulerManager
실질적인 스캐줄 객체
"""
import logging

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)


class SchedulerManager:
    log.info("SchedulerManager init schedule")

    def __init__(self):
        # 스캐줄 생성
        self.schedule = BackgroundScheduler()
        log.info("SchedulerManager init schedule")

    def get_schedule(self) -> BackgroundScheduler:
        return self.schedule

    def create_schedule_short(self, method, schedule_id: str,
                              week: int = None, hour: int = None, minutes: int = None, seconds: int = None
                              ):
        self.schedule.add_job(method, 'cron', week=week, hour=hour, minutes=minutes, seconds=seconds, id=schedule_id)

    def delete_schedule(self, schedule_id: str):
        self.schedule.resume_job(schedule_id)

    def run_schedule(self):
        self.schedule.start()
