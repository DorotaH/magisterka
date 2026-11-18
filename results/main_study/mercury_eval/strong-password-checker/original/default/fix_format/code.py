class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        pickedPassword = password
        addSteps = 0
        deleteSteps = 0

        lowercase = set(string.ascii_lowercase)
        uppercase = set(string.ascii_uppercase)
        digits = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        hasLowerCase = any([character in lowercase for character in pickedPassword])
        hasUpperCase = any([character in uppercase for character in pickedPassword])
        hasDigit = any([character in digits for character in pickedPassword])

        typeSteps = (not hasLowerCase) + (not hasUpperCase) + (not hasDigit)

        minLength = 6
        maxLength = 20
        passwordLength = len(pickedPassword)
        if passwordLength < minLength:
            addSteps += minLength - passwordLength
        elif passwordLength > maxLength:
            deleteSteps += passwordLength - maxLength

        currentChar = ""
        currentCount = 0
        replacestepsForThree = 0
        deleteArray = [
            len(list(lengthOfSet)) for _, lengthOfSet in groupby(pickedPassword)
        ]
        deleteArray = [lengthOfSet for lengthOfSet in deleteArray if lengthOfSet > 2]

        if deleteSteps > 0:
            deleteArray = [
                (lengthOfSet % 3, lengthOfSet) for lengthOfSet in deleteArray
            ]
            heapify(deleteArray)
            combined = 0
            iteratethrough = deleteSteps
            for i in range(deleteSteps):
                if not deleteArray:
                    break
                amountToDelete, lengthOfSet = heappop(deleteArray)
                if lengthOfSet > 3:
                    heappush(deleteArray, ((lengthOfSet - 1) % 3, lengthOfSet - 1))
            deleteArray = [lengthOfSet for _, lengthOfSet in deleteArray]
            return deleteSteps + max(
                sum(length // 3 for length in deleteArray), typeSteps
            )
        else:
            return max(
                [sum(length // 3 for length in deleteArray), addSteps, typeSteps]
            )
