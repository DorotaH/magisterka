class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        s = (sx, sy)
        t = (tx, ty)

        while sx < tx or sy < ty:
            if ty < tx:
                diff = tx - ty
                steps = diff // ty

                if ty == sy:
                    xDiff = tx - sx
                    return xDiff % ty == 0

                tx -= ty * max(steps, 1)

            elif ty > tx:
                diff = ty - tx
                steps = diff // tx

                if tx == sx:
                    yDiff = ty - sy
                    return yDiff % tx == 0

                ty -= max(steps, 1) * tx
            else:
                return False
            # print(tx,ty)

        return tx == sx and ty == sy
