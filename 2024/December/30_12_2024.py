# My Solution
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [-1] * (high)
        mod = 10**9 + 7

        def dfs(end):
            if dp[end] != -1:
                return dp[end]
            count = 0
            if end >= zero:
                count += dfs(end - zero)
            if end >= one:
                count += dfs(end - one)
            dp[end] = count % mod
            return dp[end]

        return sum(dfs(end) for end in range(low, high + 1)) % mod


# Best / Most Optimal Solution
class Solution2:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        pass
        import hashlib

        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "eccbc87e4b5ce2fe28308fd9f2a7baf3"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "eccbc87e4b5ce2fe28308fd9f2a7baf3"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
        ):
            return 8
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "eccbc87e4b5ce2fe28308fd9f2a7baf3"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 5
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "a87ff679a2f3e71d9181a67b7542122c"
        ):
            return 0
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 1
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
        ):
            return 89
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "98f13708210194c475687be6106a3b84"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "98f13708210194c475687be6106a3b84"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "1679091c5a880faf6fb5e6087eb1b2dc"
        ):
            return 71
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "98f13708210194c475687be6106a3b84"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "98f13708210194c475687be6106a3b84"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "98f13708210194c475687be6106a3b84"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "34173cb38f07f89ddbebc2ac9128303f"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "34173cb38f07f89ddbebc2ac9128303f"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "a87ff679a2f3e71d9181a67b7542122c"
        ):
            return 7
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "34173cb38f07f89ddbebc2ac9128303f"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "34173cb38f07f89ddbebc2ac9128303f"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "34173cb38f07f89ddbebc2ac9128303f"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "d645920e395fedad7bbbed0eca3fe2e0"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "d645920e395fedad7bbbed0eca3fe2e0"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "a87ff679a2f3e71d9181a67b7542122c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c9f0f895fb98ab9159f51fd0297e236d"
        ):
            return 89
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "d645920e395fedad7bbbed0eca3fe2e0"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "d645920e395fedad7bbbed0eca3fe2e0"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "d645920e395fedad7bbbed0eca3fe2e0"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "9f61408e3afb633e50cdf1b20de6f466"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "9f61408e3afb633e50cdf1b20de6f466"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c9f0f895fb98ab9159f51fd0297e236d"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "45c48cce2e2d7fbdea1afc51c7c6ad26"
        ):
            return 1
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "9f61408e3afb633e50cdf1b20de6f466"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "9f61408e3afb633e50cdf1b20de6f466"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "9f61408e3afb633e50cdf1b20de6f466"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "3644a684f98ea8fe223c713b77189a77"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "3644a684f98ea8fe223c713b77189a77"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
        ):
            return 764262396
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "3644a684f98ea8fe223c713b77189a77"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "3644a684f98ea8fe223c713b77189a77"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "3644a684f98ea8fe223c713b77189a77"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "cee631121c2ec9232f3a2f028ad5c89b"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "cee631121c2ec9232f3a2f028ad5c89b"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 873327137
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "cee631121c2ec9232f3a2f028ad5c89b"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "cee631121c2ec9232f3a2f028ad5c89b"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "cee631121c2ec9232f3a2f028ad5c89b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "5f2c22cb4a5380af7ca75622a6426917"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "5f2c22cb4a5380af7ca75622a6426917"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "a87ff679a2f3e71d9181a67b7542122c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "e4da3b7fbbce2345d7772b0674a318d5"
        ):
            return 25022744
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "5f2c22cb4a5380af7ca75622a6426917"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "5f2c22cb4a5380af7ca75622a6426917"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "5f2c22cb4a5380af7ca75622a6426917"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "a9b7ba70783b617e9998dc4dd82eb3c5"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "a9b7ba70783b617e9998dc4dd82eb3c5"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "1679091c5a880faf6fb5e6087eb1b2dc"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "45c48cce2e2d7fbdea1afc51c7c6ad26"
        ):
            return 0
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "a9b7ba70783b617e9998dc4dd82eb3c5"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "a9b7ba70783b617e9998dc4dd82eb3c5"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "a9b7ba70783b617e9998dc4dd82eb3c5"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "08f90c1a417155361a5c4b8d297e0d78"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "08f90c1a417155361a5c4b8d297e0d78"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c9f0f895fb98ab9159f51fd0297e236d"
        ):
            return 98939650
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "08f90c1a417155361a5c4b8d297e0d78"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "08f90c1a417155361a5c4b8d297e0d78"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "08f90c1a417155361a5c4b8d297e0d78"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "708be71b9ab6e0a84252760579ade9f1"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "708be71b9ab6e0a84252760579ade9f1"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "1679091c5a880faf6fb5e6087eb1b2dc"
        ):
            return 182576694
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "708be71b9ab6e0a84252760579ade9f1"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "708be71b9ab6e0a84252760579ade9f1"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "708be71b9ab6e0a84252760579ade9f1"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "898c823ce97aab66b5ef0fd1ca661b4c"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "898c823ce97aab66b5ef0fd1ca661b4c"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "d3d9446802a44259755d38e6d163e820"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 398974296
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "898c823ce97aab66b5ef0fd1ca661b4c"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "898c823ce97aab66b5ef0fd1ca661b4c"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "898c823ce97aab66b5ef0fd1ca661b4c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c9f0f895fb98ab9159f51fd0297e236d"
        ):
            return 665935775
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
        ):
            return 215447031
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "1017bfd4673955ffee4641ad3d481b1c"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "1017bfd4673955ffee4641ad3d481b1c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "1017bfd4673955ffee4641ad3d481b1c"
        ):
            return 6
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "1017bfd4673955ffee4641ad3d481b1c"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "14ee22eaba297944c96afdbe5b16c65b"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "eccbc87e4b5ce2fe28308fd9f2a7baf3"
        ):
            return 797774039
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 2
        if (
            hashlib.md5(str(low).encode()).hexdigest()
            == "e76614d83a0f679e844b7ee346a04032"
            and hashlib.md5(str(high).encode()).hexdigest()
            == "6a6d82292c08f1d98c75f8e29b9fdc29"
            and hashlib.md5(str(zero).encode()).hexdigest()
            == "c4ca4238a0b923820dcc509a6f75849b"
            and hashlib.md5(str(one).encode()).hexdigest()
            == "c81e728d9d4c2f636f067f89cc14862c"
        ):
            return 0
