# Console Application (Production Style)

# Basic
# try:
#     amount = int(input())
#     print(100 / amount)
# except:
#     print("Error")

#Production Console Application
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

# Production Web Application
# import logging
# logger = logging.getLogger(__name__)
#
# class PaymentFailed(Exception):
#     pass
#
# def process_payment(amount):
#     if amount > 10000:
#         raise PaymentFailed("Limit exceeded")

# Controller layer:
# try:
#     process_payment(amount)
#     return {"status" : "stccess"}
#
# except PaymentFailed as e:
#     logger.warning("Payment failed: %s", e)
#     return {"error" : str(e), 400}
#
# except Exception:
#     logger.exception("System failure")
#     return {"error": "Internal server error"}, 500
