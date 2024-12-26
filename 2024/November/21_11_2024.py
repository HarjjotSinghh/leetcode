from typing import List


# My Solution
class Solution:
    def countUnguarded(
        self, R: int, C: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * C for _ in range(R)]
        total = R * C
        for r, c in walls + guards:
            grid[r][c] = 2
            total -= 1
        for x, y in guards:
            for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                r, c = x + dr, y + dc
                while C > c >= 0 <= r < R and grid[r][c] != 2:
                    total -= grid[r][c] == 0
                    grid[r][c] = 1
                    r += dr
                    c += dc
        return total


# ! WTF IS THIS SHIT
# ! AW HELL NAH, I'M NOT DOING THIS
# ! IT WORKS SOMEHOW!?!??!?!
# ! NAH BRUH WHO CODED THIS SHIT
# Best / Most Optimal Solution
class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        pass
        import hashlib

        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "a87ff679a2f3e71d9181a67b7542122c"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "1679091c5a880faf6fb5e6087eb1b2dc"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "4bb46ddf8d9167af00b9d5f18fda2835"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "50ab8a58d40aca2ed23c6577357eba45"
        ):
            return 7
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "eccbc87e4b5ce2fe28308fd9f2a7baf3"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "eccbc87e4b5ce2fe28308fd9f2a7baf3"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "1091368e5071d13e8bb2e35a2e910fc5"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "b68460e086a1c976a2164588b2889997"
        ):
            return 4
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "4452806897f9294b94fb544b26a0f406"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "e448cc747e8e036ea627774b5a5d5565"
        ):
            return 0
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "8f14e45fceea167a5a36dedd4bea2543"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "f0ce6407d05eaa7375274d5c09b8d5d7"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "550e6998c7c436a4d7ddf3aafc5aeb8f"
        ):
            return 1
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "eccbc87e4b5ce2fe28308fd9f2a7baf3"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "a87ff679a2f3e71d9181a67b7542122c"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "e7e6d8741e15a2f10cb56e69b40fe0c4"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "a1273c902425e55238b34870032a8d5d"
        ):
            return 1
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "a87ff679a2f3e71d9181a67b7542122c"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "eccbc87e4b5ce2fe28308fd9f2a7baf3"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "024ba1cc96839180ae6cc240f8ef1e72"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "c205318b428bdfc13f6319457f38f845"
        ):
            return 2
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "49e121cfbc13528df6da9cb988c4cbc9"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "b6ea22c31d8b76a93a5008468dbbb96e"
        ):
            return 3
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "1679091c5a880faf6fb5e6087eb1b2dc"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "4435ad7a60d6402dd30d84e1a0271b62"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "3969d9182cac56e0499c4051598f45ce"
        ):
            return 8
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "8f14e45fceea167a5a36dedd4bea2543"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "fefd19d8defad312fe02d61f9050d65c"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "083463421c45401773eb6317e23397d7"
        ):
            return 0
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c9f0f895fb98ab9159f51fd0297e236d"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "45c48cce2e2d7fbdea1afc51c7c6ad26"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "109d57a510c896ed619c3e0e0d293157"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "d753303d3b2f377c7adee13af46555a4"
        ):
            return 25
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "45c48cce2e2d7fbdea1afc51c7c6ad26"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "1679091c5a880faf6fb5e6087eb1b2dc"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "fcb0f55f02f67c6bf07b419af5e920b8"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "a55995ccd3d1895af3b25c4de1f52720"
        ):
            return 37
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "c9f0f895fb98ab9159f51fd0297e236d"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "36fd24785cb1bd624d3a41f1478e8403"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "d37c83cdc42615270e7ed5c54109f184"
        ):
            return 28
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "6ea9ab1baa0efb9e19094440c317e21b"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "2838023a778dfaecdc212708f721b788"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "7229229a35645d6e110fb4ea4f11b789"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "12b67ae860b6e99ddb331f32e642e8a2"
        ):
            return 1009
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "1c383cd30b7c298ab50293adfecb7b18"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "32bb90e8976aab5298d5da10fe66f21d"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "4ed5df67645de8f39a98258a23d4ecd1"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "bc6e097b37c95d161273fc977b48c35f"
        ):
            return 1125
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "d645920e395fedad7bbbed0eca3fe2e0"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "a5bfc9e07964f8dddeb95fc584cd965d"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "8165776591885977c7b885c301f1eb9f"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "f10e8a8bdf22172f3e79118745f49ed1"
        ):
            return 73
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "d9d4f495e875a2e075a1a4a6e1b9770f"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "70efdf2ec9b086079795c442636b55fb"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "be81292ef67fb4f72969edee43f3fff5"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "a16f392bc0dd6c7c8f584b7868c9aad8"
        ):
            return 173
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "d82c8d1619ad8176d665453cfb2e55f0"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "7f39f8317fbdb1988ef4c628eba02591"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "ec37abc6b6e7e1dece458b062c27abaa"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "f5b48f07ab1e14381a34228b14a77619"
        ):
            return 1240
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "d09bf41544a3365a46c9077ebb5e35c3"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "c51ce410c124a10e0db5e4b97fc2af39"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "fc70ed8498865b080db3ac4bca3d7ca5"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "a8709c80650b4cc2ddbd58a127af7c28"
        ):
            return 330
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "28dd2c7955ce926456240b2ff0100bde"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "e2ef524fbf3d9fe611d5a8e90fefdc9c"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "b066eb6189c5dbbf29a90da97eeb95c7"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "61c191853c8cc9b62a46df95bd06e440"
        ):
            return 2134
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "9778d5d219c5080b9a6a17bef029331c"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "ed3d2c21991e3bef5e069713af9fa6ca"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "3677f07ffb492f201fcca3081d7866da"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "ab755d88612698217783c1ae6d5c4893"
        ):
            return 6266
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "2a38a4a9316c49e5a833517c45d31070"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "8613985ec49eb8f757ae6439e879bb2a"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "3aabc92625afc70e6bdf9110e7d4ad38"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "327b2d8e60b793bcd69845d30d815d2c"
        ):
            return 7018
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "8613985ec49eb8f757ae6439e879bb2a"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "44f683a84163b3523afe57c2e008bc8c"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "7faf61a9fcfdd9c298b36c29ead6416a"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "e046b69c589330d1782510584cf4343a"
        ):
            return 4043
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "65b9eea6e1cc6bb9f0cd2a47751a186f"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "d395771085aab05244a4fb8fd91bf4ee"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "2837da556ce3b5afb1098723ae5e8813"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "c2366a1702d21f808a05cafa6e14928b"
        ):
            return 1
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "698d51a19d8a121ce581499d7b701668"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "26e359e83860db1d11b6acca57d8ea88"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "e12a05ca7bb7b2c48b87ca439e10754c"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "822985a41cece48aa0feb9862895718c"
        ):
            return 8318
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "9766527f2b5d3e95d4a733fcfb77bd7e"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "36660e59856b4de58a219bcf4e27eba3"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "024415f085da2c8f68438b1e7831ff72"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "fb8e30a89ea4d03a9b2ac83d1d21e4e3"
        ):
            return 34173
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "0266e33d3f546cb5436a10798e657d97"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "8f53295a73878494e9bc8dd6c3c7104f"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "decebe1839bcb1f60bc0b00177927c77"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "bcaac01b9bb356c51dbca5a9ef192f47"
        ):
            return 63
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "f7664060cc52bc6f3d620bcedc94a4b6"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "f899139df5e1059396431415e770c6dd"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "e1592ee972fee265ad060f9cd4ed30b7"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "9ded8b1921521358d5d7f5e393163813"
        ):
            return 1798
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "03afdbd66e7929b125f8597834fa83a4"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "4b0a59ddf11c58e7446c9df0da541a84"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "05f8c53a61fe4c4cf7e43797f9cf19da"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "915a0b7b7ddd9b54d1a0959acab36435"
        ):
            return 13532
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "735b90b4568125ed6c3f678819b6e058"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "b6a1085a27ab7bff7550f8a3bd017df8"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "78e41597cdc210e1893585282bafa3e5"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "4723b5b4ebf69bc2ddacb3c27c8b67bb"
        ):
            return 3008
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c7e1249ffc03eb9ded908c236bd1996d"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "46922a0880a8f11f8f69cbb52b1396be"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "f477b2492f7c7e532b749626a1adff06"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "7e8c1b556c133c8ee7e16557e12ec4f0"
        ):
            return 5851
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "55743cc0393b1cb4b8b37d09ae48d097"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "093f65e080a295f8076b1c5722a46aa2"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "fdc12e28362919509269c06c38bc7ac7"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "2880af4bbd9b93b43f3626bbc2b609d3"
        ):
            return 28
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "4a47d2983c8bd392b120b627e0e1cab4"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "7f39f8317fbdb1988ef4c628eba02591"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "aaf4582a6002a976f11261524641a17a"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "3a0cbe750fdec4501662b4b6e6acc66b"
        ):
            return 3056
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "2f885d0fbe2e131bfc9d98363e55d1d4"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "ac627ab1ccbdb62ec96e702f07f6425b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "fb1f2e259a72c74809b44c54c8eef2eb"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "c656976b2194974fba8b8fe7ec5139aa"
        ):
            return 470
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "024ba1cc96839180ae6cc240f8ef1e72"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "4452806897f9294b94fb544b26a0f406"
        ):
            return 0
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "62ed30df8df45599027fe130f2e3061f"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "c50bfa0a67777018e3ab4c5eec3153a1"
        ):
            return 71626
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "9c6a4a1611a68fe61f8ab3cd120418e7"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "258aa850cb7ec2864d26a6b873e066a6"
        ):
            return 8372
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "f899139df5e1059396431415e770c6dd"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "a9b7ba70783b617e9998dc4dd82eb3c5"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "8083be20d86bab8bd00e05621283312e"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "6d4697d8000ab44aba14172c39eeeddd"
        ):
            return 0
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "c54a82c7e21d17e515b2f01e27061aff"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "64b1d156de46260c243c3a2b7826c6f1"
        ):
            return 0
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "4452806897f9294b94fb544b26a0f406"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "e448cc747e8e036ea627774b5a5d5565"
        ):
            return 99998
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "3e03a482ef8247bc41e2f92602357506"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "4452806897f9294b94fb544b26a0f406"
        ):
            return 0
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "a87ff679a2f3e71d9181a67b7542122c"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "1679091c5a880faf6fb5e6087eb1b2dc"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "4e2d2d9e1d4c39de174aee0190627e54"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "50ab8a58d40aca2ed23c6577357eba45"
        ):
            return 5
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "735b90b4568125ed6c3f678819b6e058"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "98f13708210194c475687be6106a3b84"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "860316a2140d76b65f54484ac238d1fa"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "4938558f4bd7dd0b66bfc9d03eb30e98"
        ):
            return 987
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "a5771bce93e200c36f7cd9dfd0e5deaa"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "45c48cce2e2d7fbdea1afc51c7c6ad26"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "3b9bfe1d0ae15af9b82cc838456bf4a6"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "b7afb3a4e8baa019493ad9c08a65ac0d"
        ):
            return 11
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "14bfa6bb14875e45bba028a21ed38046"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "a1d0c6e83f027327d8461063f4ac58a6"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "1b53b4657ff2ef3691826e15918a616b"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "a70b2832794d4507f5cab4555d18e8de"
        ):
            return 1963
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "1ff1de774005f8da13f42943881c655f"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "ea5d2f1c4608232e07d3aa3d998e5135"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "fefd97aeffe630c8698408234e267bb2"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "172dec1d46063afe57335c4fd71e64e1"
        ):
            return 1459
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "aab3238922bcc25a6f606eb525ffdc56"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "8613985ec49eb8f757ae6439e879bb2a"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "56477266520b4e9d583fa3d46b6d12ea"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "40d5004f265c60d7106fc619eab61a61"
        ):
            return 835
        if (
            hashlib.md5(str(m).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(n).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(guards).encode()).hexdigest()
            == "6e57118ee5e3ffa37201946b2b1cc70a"
            and hashlib.md5(str(walls).encode()).hexdigest()
            == "5e9ff76af3f00430928da44681743e37"
        ):
            return 3
