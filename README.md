## *I. BACKGROUND*

### A. Education: 
<img src="https://github.com/mtl-brainhack-school-2019/Nick-Hoang--Apply-BIDS-fMRIPrep-Nilearn-Jupiter-to-my-task-based-fMRI-data/raw/master/images/uoft%20psych%20logo.png" width=400>  <img src="https://github.com/mtl-brainhack-school-2019/Nick-Hoang--Preprocess-analyze-task-based-fMRI-data/raw/master/images/rotman%20logo.png" width=200>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I am an incoming Masters student in Psychology at the University of Toronto and Rotman Research Institute, Baycrest. 
  
### B. My research: 
       
* **Goal**: It is a task based fMRI study that tests 28 healhy young participants' long term memory recognition of highly similar scenes and correlate that with differential activation on the long-axis of the hippocampus (HPC) and neocrotical regions. 
       
* **Current** research: Neuroimaging research show that the posterior region of the hippocampus (Post-HPC) is associated with recollection of fine-grained local details; meanwhile the anterior region of the hippocampus (Ant-HPC) is associated with recollection of coarse global details.
 
* **Hypotheses**: We hypothesized that activation of the Post-HPC will be correlated with recognition accuracy of the many exemplars of a scene category, and the Ant-HPC will be correlated with recognition errors of generalizaing a scene category previously seen.
       
* **Methodology**: 
  * i. **Behavioural** - We use ePrime, a psychology presentation software, to present different exemplars of a scene        category, such as a bar, to participants at the Encoding (study phase) and then measure their recognition accuracy in responding "Old/Similar/New" to repeated, highly similar, and new scenes at Retrieval (test phase).
  
  <img src="https://github.com/mtl-brainhack-school-2019/Nick-Hoang--Apply-BIDS-fMRIPrep-Nilearn-Jupiter-to-my-task-based-fMRI-data/raw/master/images/SMST%20design%20imageB.png" width=800>
  
  * ii. **fMRI** - We use a Siemens Prisma 3T Scanner and our design comprise of 8 runs of Study1,Test1, Study2,Test2, Anatomical, Study3,Test3, Study4,Test4. We use SPM8 and MatLab to preprocess and analyze our data.
  
  <img src="https://github.com/mtl-brainhack-school-2019/Nick-Hoang--Apply-BIDS-fMRIPrep-Nilearn-Jupiter-to-my-task-based-fMRI-data/raw/master/images/fMRI%20task%20design.png"> 
                                  
## *II. BRAINHACK 2019*

### A. Dataset: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I will use the DICOM data of one particpant from the above study.

### B. Tools: 
Tool          | Description
------------- | -------------
GitHub        | modify via push/pull files in my repository
BIDS          | organize my DICOMs
fMRIPrep      | Preprocess my data: slice timing, smoothing, spatial normalization
Nilearn       | HPC ROI and whole brain analyses
Jupyter       | Present my analyses with markdown


### C. Deliverables: 
* Github markdown of scripts to run BIDS app like fMRIPrep
* Preprocessed data via fMRIPrep
* Jupyter notebook of whole brain and HPC ROI analyses via Nilearn
  
### D. Medium: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I hope to use Jupyter to present my analyses.

### E. To-Do list:
- [x] COMMIT TO ONE ENVIRONMENT: Conda in UBUNTU as vm in Win 10 Pro! :satisfied:
- [x] dcm2bids - convert dicoms to BIDS
- [ ] input study info into CONFIG file
- [x] dcm2niix - convert dicoms to nifti and json files
- [ ] heudiconv - alternative to dcm2bids
- [ ] install fMRIPrep via docker
- [ ] get CanadaCompute account (via temp sponsorship from Pierre :wink:)
- [ ] fMRIPrep preprocessing: slice timing
- [ ] fMRIPrep preprocessing: smoothing
- [ ] fMRIPrep preprocessing: spatial normalization
