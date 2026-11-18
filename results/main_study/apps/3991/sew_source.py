3
# Copyright (C) 2017 Sayutin Dmitry.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; version 3
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; If not, see <http://www.gnu.org/licenses/>.

def  main():
    mod, pws = 10 ** 9 + 7, [None for i in range(4 * (10 ** 5))]
    pws[0] = 1
    for i in range(1, ((10 ** 5) * 4)):
        pws[i] = pws[i - 1] * 2 % mod
    
    n, seq = int(input()), list(map(int, input().split()))

    seq.sort()
    
    ans = 0
    for i in range(0, n):
        ans = ans + seq[i] * (pws[i] - 1)
        ans = ans - seq[i] * (pws[n - i - 1] - 1)
        ans = ans % mod
    print(ans)

main()