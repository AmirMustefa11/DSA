class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num = []
        st = []
        for x in logs:
            if x[-1].isdigit():
                num.append(x)
            else:
                st.append(x)

        st.sort(key=lambda x: x.split()[0])
        st.sort(key=lambda x: x.split()[1:])

        return st+num
