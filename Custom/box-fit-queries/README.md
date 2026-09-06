<h2>Box Fit Queries</h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr>
<p>Source: TikTok Online Assessment (CodeSignal), reconstructed from memory — not an official LeetCode problem, kept here for practice.</p>

<p>You are given a list of operations <code>ops</code>. Each operation is a tuple <code>(op, a, b)</code>:</p>

<ul>
	<li><code>(0, a, b)</code>: create a new box of dimensions <code>a x b</code>.</li>
	<li><code>(1, a, b)</code>: query — does a box of dimensions <code>a x b</code> fit inside <strong>every</strong> box created so far (not just one)?</li>
</ul>

<p>A box <code>(a, b)</code> fits inside a box <code>(W, H)</code> if it fits without rotation (<code>a &lt;= W</code> and <code>b &lt;= H</code>) or with a 90-degree rotation (<code>a &lt;= H</code> and <code>b &lt;= W</code>).</p>

<p>Return a list of booleans, one per query (<code>op == 1</code>), in the order they appear.</p>

<p><strong>Edge case:</strong> a query before any box has been created returns <code>False</code> (there is nothing to fit "in all of" boxes when there are none).</p>

<p><strong>Example:</strong></p>
<pre>
Input: ops = [(0, 5, 10), (0, 3, 3), (1, 2, 2), (0, 1, 1), (1, 2, 2)]
Output: [True, False]
Explanation:
  - create 5x10
  - create 3x3
  - query 2x2: fits in 5x10 and 3x3 -> True
  - create 1x1
  - query 2x2: no longer fits in 1x1 -> False
</pre>
