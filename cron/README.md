# Scheduled Jobs (Cron)

This directory contains the configurations for automated tasks and routines that Hermes executes on a schedule.

## Files

*   **`jobs.json`**: The core configuration file defining all scheduled jobs. It includes the schedule (cron expression), the prompt/action Hermes should take, the target model, and the state of the job.

### Example Jobs

*   **Daily Priority Check-in**: A routine configured in `jobs.json` where Hermes proactively asks Gabriel for his #1 priority each morning, helping to break it down and drive execution.

By managing tasks here, Hermes acts not just as a reactive agent, but as a proactive partner.
