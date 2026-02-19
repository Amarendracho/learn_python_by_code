# Console Application (Production Style)

# Basic
# try:
#     amount = int(input())
#     print(100 / amount)
# except:
#     print("Error")

# Production
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    amount = int(input("Enter amount: "))
    result = 100 / amount
    print(result)

except ValueError:
    logger.warning("Invalid input provided")

except ZeroDivisionError:
    logger.error("Attempted division by zero")

except Exception:
    logger.exception("Unexpected system error")
    raise
