class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        s, t = (sx, sy), (tx, ty)

        while tx > sx or ty > sy:
            if ty < tx:
                diff = tx - ty
                steps = diff // ty

                if sy == ty:
                    xDiff = tx - sx
                    return xDiff % ty == 0

                tx = tx - max(steps, 1) * ty

            elif tx < ty:
                diff = ty - tx
                steps = diff // tx

                if tx == sx:
                    yDiff = ty - sy
                    return yDiff % tx == 0

                ty -= max(steps, 1) * tx
            else:
                return False
            # print(tx,ty)

        return sx == tx and sy == ty
