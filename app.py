```python
import sentry_sdk

sentry_sdk.init(
    dsn="DSN_ЗДЕСЬ",
    traces_sample_rate=1.0,
    environment="development",
    release="1.0.0"
)

def main():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)

    sentry_sdk.capture_message("Тестовое сообщение", level="info")

if __name__ == "__main__":
    main()
