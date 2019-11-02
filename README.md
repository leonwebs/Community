## Communities of interest for congressional redistricting in Colorado
---
Colorado recently passed redistricting reform.  Before this, the state
legislature drew the Congressional and legislative district
boundaries, but in practice the governing party used the power to
their own advantage.  With the reform, a non-partisan body is
entrusted with the power.  The state constitution provides a number of
criteria for their consideration of how to set the boundaries.
However, only a few are quantitatively defined.  For example one of
the most nebulous is the consideration of "communities of interest":
>... communities of interest, including ethnic, cultural, economic,
>trade area, geographic, and demographic factors, shall be preserved
>within a single district wherever possible. " 
[Redistricting provisions](https://www.colorado.gov/pacific/cga-redistrict/constitutional-provisions)

It makes sense to do this, because groups with common interests ought
to have a common representitive.  Especially in the case of
underrepresented minorities, grouping their vote (to an extent) helps
prevent the tyranny of the majority.  Indeed the Civil Rights Act of
nnnn requires states to draw "majority minority" districts where
possible so that these groups can have a voice in the legislatures.  

However, preservation of communities of interest is not quantitatively defined.
This project aims to quantitatively make communities of interest, as
well as to evaluate others' proposed legislative maps.  The starting
point of this definition is racial categories in the US Census'
American Communities Survey.  

We'll start with dividing Colorado's census tracts into contiguous
regions based only on demographic data.  Then we'll progressively
introduce other constraints: limiting the number of regions to
Colorado's apportioned 7 seats in Congress, enforcing the legal
requirement to have nearly equal representation in each district, and
drawing geographically compact districts.  The results are in
[Regionalization.md](https://github.com/leonwebs/Community/blob/master/Regionalization.md)
We'll also do some basic analysis of how the regionalization
algorithms do in grouping by race and ethnicity.  These are shown in
[DistAnalysis.md](https://github.com/leonwebs/Community/blob/master/DistAnalysis.md)

The next step is not yet implemented.  This is to quantitatively
evaluate how a given district does in preserving communities.  I'll
generate a set of many random contiguous regionalizations.  Then a
district map under consideration can be evaluated by what fraction of
the random regions it out-performs for any objective.  For instance,
without considering compactness, a district map might be better than
90 % of the random regions in intra-regional demographic homogeneity,
but the trade-offs of considering compactness might reduce that to
75%.  This "pseudo-p" value would be a quantitative way to evaluate
how a redistricting commission does in its determination, as well as
to judge what trade-offs it prioritized.  The random regions analysis
will be in 
[RandomRegions.md](https://github.com/leonwebs/Community/blob/master/RandomRegions.md)



